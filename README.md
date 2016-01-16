# Lektor Surge Publisher Plugin

Publishes your [Lektor](https://www.getlektor.com/) site to [Surge](https://surge.sh/).

## Installation

Add lektor-surge to your project from command line:

```
lektor plugins add lektor-surge
```

See [the Lektor documentation for more instructions on installing plugins](https://www.getlektor.com/docs/plugins/).

## Configuration

Configure Surge in your `.lektorproject` file:

```ini
[servers.surge]
target = surge:my-domain.com
```

To force all traffic to HTTPS, update your `.lektorproject` file:

```ini
[servers.surge]
target = surge+https:my-domain.com
```

For more information, see the [Surge guide to HTTPS](https://surge.sh/help/using-https-by-default).

## Deployment

Deploy your site with Lektor from the command line:

```
lektor deploy surge
```
