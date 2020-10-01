---
_db_id: 174
content_type: topic
ready: true
title: Data validation and quality control
---

## Prevention first!

- Design surveys and tools in such a way that minimises user error and measurement error

## Inspect the data

- Completeness:

  - How complete is the data?
  - It's very important to differentiate between data that is missing and data that has a zero value! These mean very different things!
  - QC: get count of missing observations
  - QC: Are all important variables measured?

- Measurement accuracy:

  - Do the data represent the true value of what is being measured?
  - Could be incorrect because of incorrect entry, unreliable measurement, incorrectly functioning/ broken machines, etc.
  - QC: check that data are within allowable bounds (e.g. no percentages higher than 100%)
  - QC: check measure reliability
  - QC: check measure validity (e.g., compare measures that should be similar - the measure should not be biased or contaminated)
  - QC: Visually inspect the data to see whether it looks as it should - i.e. is the mean, range and distribution what we would expect? Are there outliers?
  - Documentation: Measurement imprecision should be noted in the documentation (e.g. the distance measure gives distance to the closest 100km)

- Calculation accuracy: Are the calculation functions performing the correct calculations and are they working as they should?

  - QC: unit tests to check that functions are working as they should
  - QC: Visually inspect to see that the output matches what you would expect

- Integrity:
  - On storage, data values are standardized according to a data model and/or data type.
  - All characteristics of the data must be correct – e.g. dates, integers.
  - Data must stay secure and correct over its lifespan: data cannot be modified in an unauthorized or undetected manner.
  - Minimise duplication of data
  - Store the original, raw data separately from processed data

## Know the data content and pipeline

Individuals who know the data best are very important to successfully validating the data! Alternatively, get out on the ground and get to know the data process and content yourself!

## Documentation

An audit trail should always be available, i.e. how the data is collected, transformed and stored should be documented so that it is clear at which step of
the process problems may have crept in.

## References

[Data quality assurance in data warehousing](https://www.blue-granite.com/blog/overview-of-data-quality-assurance-in-data-warehousing)  
[The Challenges of Data Quality and Data Quality Assessment in the Big Data Era](https://datascience.codata.org/articles/10.5334/dsj-2015-002/)