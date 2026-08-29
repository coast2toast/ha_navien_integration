# Navien NaviLink Home Assistant Integration

Persistent project workspace for researching, developing, testing, and reviewing a Home Assistant custom integration for Navien NaviLink-connected NPE-2 equipment.

## Intended structure

- `custom_components/navien_navilink/` — Home Assistant custom integration
- `tests/` — automated tests
- `docs/` — protocol research, setup notes, and user documentation

## Development expectations

- Keep credentials and device tokens out of the repository.
- Prefer local-device communication where technically possible.
- Document any cloud dependency and API limitations.
- Verify changes with tests before marking Kanban work complete.
