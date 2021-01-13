"""
This is a Python3.7 script that makes sure that markdown files are named correctly.
It also highlights any metadata problems (specifically missing titles)
"""

from pathlib import Path
import frontmatter
import yaml
import logging
logging.basicConfig(level=logging.WARN)


with open("flavours.yaml", "r") as f:
    option_groups = yaml.load(f, Loader=yaml.FullLoader)
l = [list(option_groups.keys())] + list(option_groups.values())
flat_options = [s for sub in l for s in sub]

allowed_submission_types = [
    "repo",  # we create a repo and own it
    "link",  # they give us a link to a document they own
    "continue_repo",  # this is part of a multi part project. Use the repo that already exists. If this option is used then must include the 'from_repo' frontmatter key
    "nosubmit",
]


def check_all_frontmatter_and_directory_names(path):
    location = Path(path)
    assert location.is_dir(), location
    assert (
        str(location) == str(location).lower()
    ), f"location has uppercase letters: {location}"

    assert str(location) == str(location).replace(
        " ", ""
    ), f"location has illegal characters: {location}"

    for child in location.iterdir():
        if child.is_dir():
            check_all_frontmatter_and_directory_names(child)
        else:
            check_one_file_frontmatter(child)



class IdChaecker:
    seen_syllabuses = {}
    seen_content_items = {}

    @classmethod
    def check(cls, db_id, title, file_path):
        if file_path.name == "_index.md":
            # we are dealing with normal content items
            seen = cls.seen_content_items 
        else:
            seen = cls.seen_syllabuses

        if db_id in seen:
            raise Exception(f"Repeated id! {db_id} found at {file_path} ({title})AND {seen[db_id]['file_path']} ({seen[db_id]['title']})")
        seen[db_id] = {
            "title": title,
            "file_path": file_path,
        }


def check_one_file_frontmatter(file_path):
    """ given the path to a markdown file, make sure that the frontmatter includes
    the required metadata
    """
    logging.info(f"checking frontmatter for {file_path}")
    name = file_path.name
    if not name.endswith(".md"):
        return
    
    if name != "_index.md":
        # only checking content items
        return 
    front = frontmatter.load(file_path)

    required = ["title","content_type"]
    allowed = [
        "_db_id",
        "pre",
        "weight",
        "ready",
        "date",
        "disableToc",
        "todo",
        
        "prerequisites",
        "tags",
        "story_points",
        "available_flavours",
        "topic_needs_review",

        "ncit_standards",
        "ncit_specific_outcomes"
    ]

    if "_db_id" in front:
        IdChaecker.check(front["_db_id"], front["title"], file_path)

    is_project = front.get('content_type') == "project"

    if is_project:
        required.append("submission_type")

    hard_prereq = front.get("prerequisites", {}).get("hard", [])

    if "submission_type" in front:
        assert (
            front["submission_type"] in allowed_submission_types
        ), f"{file_path} invalid submission type: {front['submission_type']}"
        if front["submission_type"] == "continue_repo":
            required.append("from_repo")

            assert (
                front["from_repo"] in hard_prereq
            ), f"{file_path}: expected hard prepreq: '{front['from_repo']}'\nonly found: {hard_prereq}"
        if front["submission_type"] != "nosubmit":
            required.append("available_flavours")
        if front["submission_type"] == "repo":
            allowed.append("template_repo")

    for key in front.keys():
        if key not in required + allowed:
            logging.warning(f"{file_path} has unrecognized frontmatter: {key}")
            continue

    for key in required:
        if key not in front.keys():
            logging.error(f"{file_path} has MISSING frontmatter: {key}")
            continue

    if "available_flavours" in front and front.get("submission_type") != "nosubmit":
        for option in front["available_flavours"]:
            assert option in flat_options, f"{option} not in {flat_options}"


def check_contentlinks_ok():
    import os

    os.system("hugo")
    os.system('grep -r "contentlink-missing" public') 
    # os.system('grep -r "contentlink-todo" public')  


if __name__ == "__main__":
    check_all_frontmatter_and_directory_names("content")
    check_contentlinks_ok()

