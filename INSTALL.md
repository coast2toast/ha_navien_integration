# Navien NaviLink NPE-2 — Home Assistant installation

This package contains the `navien_navilink_wh` custom integration from
https://github.com/lasswellt/navien-homeassistant, release `2026.06.03`
(commit `b8c595658c5fb3b90bfbcc2818c21df91cfbe055`). It is MIT-licensed and
has been validated by its maintainer against a live NaviLink-connected NPE-2.

## Requirements

- Home Assistant 2024.12.0 or newer
- A working NaviLink account and a NaviLink-connected heater
- Home Assistant must be able to reach Navien's cloud service

## Recommended installation (HACS)

1. Open Home Assistant.
2. Go to **HACS → Integrations**.
3. Open the three-dot menu and select **Custom repositories**.
4. Enter `https://github.com/lasswellt/navien-homeassistant`.
5. Select category **Integration**, then add it.
6. Search for and install **Navien NaviLink Water Heater**.
7. Restart Home Assistant.
8. Go to **Settings → Devices & services → Add integration**.
9. Search for **Navien NaviLink Water Heater** and follow the setup flow.

## Manual installation from this ZIP

1. Extract the ZIP.
2. Copy `custom_components/navien_navilink_wh` into Home Assistant's
   `/config/custom_components/` directory. The final manifest must be at:
   `/config/custom_components/navien_navilink_wh/manifest.json`.
3. Restart Home Assistant.
4. Go to **Settings → Devices & services → Add integration**.
5. Search for **Navien NaviLink Water Heater**.
6. Enter the same email address and password used by the NaviLink mobile app.
7. Select the NaviLink gateway.

Do not place credentials in `configuration.yaml`, logs, or support messages.

## Expected entities

The integration can expose:

- A `water_heater` entity with power/away mode, current temperature, and target temperature
- Power and on-demand recirculation switches when supported by the unit
- Inlet/outlet temperature, hot-water flow, gas usage, and heating-power sensors
- Diagnostic sensors and binary sensors for faults and cloud connectivity

Some diagnostic entities are disabled by default. Open the device's entity list
to enable any needed diagnostics.

## Validation performed for this package

- Python bytecode compilation completed successfully.
- All 45 upstream automated tests passed under Python 3.13 and Home Assistant 2026.2.3.
- Test coverage was 96% across 874 executable statements.
- The source explicitly supports `DeviceSorting.NPE2` and includes Fahrenheit
  and Celsius NPE-2 protocol conversion tests.

A live login/device test was not performed because NaviLink credentials were not
provided. The integration is cloud-dependent and unofficial; Navien may change
the service without notice.

## Troubleshooting

- If setup says authentication is invalid, confirm the credentials in the NaviLink app.
- If entities are unavailable, confirm the gateway is online and Home Assistant has internet access.
- Brief unavailability during the approximately hourly cloud token reconnect can be normal.
- Download redacted diagnostics from the integration's device page when opening an upstream issue:
  https://github.com/lasswellt/navien-homeassistant/issues
