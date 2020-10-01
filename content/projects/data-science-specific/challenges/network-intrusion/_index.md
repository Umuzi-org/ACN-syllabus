---
_db_id: 250
available_flavours:
- python
content_type: project
pre: '<b> HARD: </b>'
ready: true
submission_type: repo
title: Network Intrusion
---

Software to detect network intrusions protects a computer network from unauthorized users, including perhaps insiders. The intrusion detector learning task is to build a predictive model (i.e. a classifier) capable of distinguishing between "bad" connections, called intrusions or attacks, and "good" normal connections.

### Background

The 1998 DARPA Intrusion Detection Evaluation Program was prepared and managed by MIT Lincoln Labs. The objective was to survey and evaluate research in intrusion detection. A standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment, was provided.

Lincoln Labs set up an environment to acquire nine weeks of raw TCP dump data for a local-area network (LAN) simulating a typical U.S. Air Force LAN. They operated the LAN as if it were a true Air Force environment, but peppered it with multiple attacks.

The raw training data was about four gigabytes of compressed binary TCP dump data from seven weeks of network traffic. This was processed into about five million connection records. Similarly, the two weeks of test data yielded around two million connection records.

A connection is a sequence of TCP packets starting and ending at some well defined times, between which data flows to and from a source IP address to a target IP address under some well defined protocol. Each connection is labeled as either normal, or as an attack, with exactly one specific attack type. Each connection record consists of about 100 bytes.

This data was adjusted from the original and was taken from the 1999 KDD Cup. The data set contains 43 features per record, with 41 of the features referring to the traffic input itself and the last two are labels (whether it is a normal or attack) and Score (the severity of the traffic input itself).

## Instructions

Create a classifier to predict good vs bad connections. Go through all the relevant steps of [CRISP Data Mining](https://www.ibm.com/support/knowledgecenter/SS3RA7_15.0.0/com.ibm.spss.crispdm.help/crisp_overview.htm) to decide on the best model to use and to build the classifier.

The compressed data file can be found [here](kddcup.data.gz).

## Outcome

Attacks fall into four main categories:

- DOS: denial-of-service, e.g. syn flood
- R2L: unauthorized access from a remote machine, e.g. guessing password
- U2R: unauthorized access to local superuser (root) privileges, e.g., various - "buffer overflow" attacks
- probing: surveillance and other probing, e.g., port scanning

#### Attack types:

- back
- buffer_overflow
- ftp_write
- guess_passwd
- imap
- ipsweep
- land
- loadmodule
- multihop
- neptune
- nmap
- normal
- perl
- phf
- pod
- portsweep
- rootkit
- satan
- smurf
- spy
- teardrop
- warezclient
- warezmaster

## Features:

### Table 1: Basic features of individual TCP connections.

| feature name   | description                                                  | type       |
| -------------- | ------------------------------------------------------------ | ---------- |
| duration       | length (number of seconds) of the connection                 | continuous |
| protocol_type  | type of the protocol, e.g. tcp, udp, etc.                    | discrete   |
| service        | network service on the destination, e.g., http, telnet, etc. | discrete   |
| src_bytes      | number of data bytes from source to destination              | continuous |
| dst_bytes      | number of data bytes from destination to source              | continuous |
| flag           | normal or error status of the connection                     | discrete   |
| land           | 1 if connection is from/to the same host/port; 0 otherwise   | discrete   |
| wrong_fragment | number of 'wrong'' fragments                                 | continuous |
| urgent         | number of urgent packets                                     | continuous |

### Table 2: Content features within a connection suggested by domain knowledge.

| feature name       | description                                           | type       |
| ------------------ | ----------------------------------------------------- | ---------- |
| hot                | number of 'hot' indicators                            | continuous |
| num_failed_logins  | number of failed login attempts                       | continuous |
| logged_in          | 1 if successfully logged in; 0 otherwise              | discrete   |
| num_compromised    | number of 'compromised' conditions                    | continuous |
| root_shell         | 1 if root shell is obtained; 0 otherwise              | discrete   |
| su_attempted       | 1 if 'su root' command attempted; 0 otherwise         | discrete   |
| num_root           | number of 'root' accesses                             | continuous |
| num_file_creations | number of file creation operations                    | continuous |
| num_shells         | number of shell prompts                               | continuous |
| num_access_files   | number of operations on access control files          | continuous |
| num_outbound_cmds  | number of outbound commands in an ftp session         | continuous |
| is_hot_login       | 1 if the login belongs to the 'hot' list; 0 otherwise | discrete   |
| is_guest_login     | 1 if the login is a 'guest' login; 0 otherwise        | discrete   |

### Table 3: Traffic features computed using a two-second time window.

| feature name                                                          | description                                                                                 | type       |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------- |
| count                                                                 | number of connections to the same host as the current connection in the past two seconds    | continuous |
| Note: The following features refer to these same-host connections.    |
| serror_rate                                                           | % of connections that have SYN errors                                                       | continuous |
| rerror_rate                                                           | % of connections that have REJ errors                                                       | continuous |
| same_srv_rate                                                         | % of connections to the same service                                                        | continuous |
| diff_srv_rate                                                         | % of connections to different services                                                      | continuous |
| srv_count                                                             | number of connections to the same service as the current connection in the past two seconds | continuous |
| Note: The following features refer to these same-service connections. |
| srv_serror_rate                                                       | % of connections that have SYN errors                                                       | continuous |
| srv_rerror_rate                                                       | % of connections that have REJ errors                                                       | continuous |
| srv_diff_host_rate                                                    | % of connections to different hosts                                                         | continuous |