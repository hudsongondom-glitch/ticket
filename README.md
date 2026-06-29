# Online Ticketing System

Requirements engineering and software design assignment for an online ticketing
platform supporting the reservation and purchase of event tickets and season
pass subscriptions.

## Repository structure

```
ticketing/
├── README.md
├── .gitignore
├── requirements.txt
├── report/
│   ├── Ticketing_Assignment.docx
│   ├── Ticketing_Assignment.pdf
│   └── figures/
├── diagrams/
│   ├── bpmn.drawio
│   ├── usecase.drawio
│   ├── domain.drawio
│   └── sequence.drawio
├── src/
│   └── celsius.py
├── tests/
│   └── test_celsius.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Report

The full assignment report, covering the BPMN diagram, use case diagram and
scenarios, user stories, domain model, sequence diagram, unit testing, and use
of Git, is available in `report/Ticketing_Assignment.docx` and
`report/Ticketing_Assignment.pdf`.

## Diagrams

All diagrams are provided as editable `.drawio` files under `diagrams/` and can
be opened directly with [draw.io](https://app.diagrams.net/):

- `bpmn.drawio` — BPMN process for reserving and purchasing tickets, including
  subscription to season passes.
- `usecase.drawio` — Use case diagram of the system.
- `domain.drawio` — Domain model.
- `sequence.drawio` — Sequence diagram of the ticket purchase process.

## Unit testing

`src/celsius.py` implements `celsius_to_fahrenheit`, a temperature conversion
function. Its test suite is in `tests/test_celsius.py` and covers normal
values, the freezing and boiling points of water, negative and fractional
temperatures, absolute zero, invalid input types, and boundary cases.

Install dependencies and run the tests with:

```
pip install -r requirements.txt
pytest tests/
```

Tests are also run automatically on every push via the GitHub Actions
workflow defined in `.github/workflows/tests.yml`.
