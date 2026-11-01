# Django — Python

**Reviewed:** 2026-11-01 · [Framework index](README.md)

## Fit
Data-centric web application needing built-in ORM, admin interface, authentication/forms and conventional server-rendered workflows.

## Anti-fit
Tiny API without admin/ORM needs, pure inference worker or a project already using a suitable API framework. Avoid importing Django just to obtain its ORM in a simple service without validating overhead.

## Compatibility
Match Django/Python/database combinations against official supported versions; migrations and async views have their own limitations. Hosting and database compatibility vary by runtime/driver.

## Maturity & maintenance
Official release and supported-version policy exists, including LTS releases; **verify the applicable version’s support end date** before choice, not a generic evergreen status.

## Licensing
Django distribution is **BSD 3-Clause**; data/database drivers, admin extensions and SaaS hosting may have different terms.

## Operational / test evidence needed
Migration reversibility, admin permissions, CSRF, auth/session, DB queries/locks, integration tests, backup/restore, security update path, error telemetry and hosting costs.

## Official evidence
- [Django overview](https://docs.djangoproject.com/en/stable/intro/overview/)
- [Supported versions](https://www.djangoproject.com/download/)
- [Django software license](https://www.djangoproject.com/foundation/faq/#license)
