# LedgerLink

An explainable data reconciliation engine.

## What is LedgerLink?

LedgerLink is an open-source project designed to help businesses
identify and investigate inconsistencies between related records.

For example:

- A business orders 100 units.
- 98 units are recorded as delivered.
- The supplier invoices the business for 100 units.

LedgerLink detects the discrepancy and provides the information
needed to investigate it.

## Why?

Business data often comes from different sources.

These sources may disagree because of:

- missing records
- incorrect quantities
- duplicate records
- incorrect prices
- inconsistent information
- data-entry mistakes

LedgerLink aims to make these discrepancies easier to detect,
understand, and investigate.

## Core idea

LedgerLink should not simply say:

> "Something is wrong."

It should help answer:

> "What is wrong, where did the difference come from,
> and what evidence supports it?"

## Project status

🚧 Early development.

The first version will focus on CSV data,
Python, SQL, and PostgreSQL.

## Long-term vision

LedgerLink is intended to become a modular system where
developers can extend its reconciliation and data-quality
capabilities with their own rules, connectors, and tools.

## License

License to be decided.
