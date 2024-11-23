# Ansible Collection - mrmolybdaen.molybdaen

This collection is a result of my work. It aims to standardize deployments of Debian based web servers, mostly LAMP stacks.

The aim of this collection is to move from Infrastructure as Code (IaC) to a Configuration as Code like model as well.
This means host variables can be used to create YAML based configuration which will get translated via Jinja2 templates
into the actual configuration format.

Security is oriented on CIS benchmarks where available and is mostly optimized for web servers with a limited amount of confidential data.

> **IMPORTANT:**
> If your servers are running in an environment with high confidentiality, such as medical, finance, universities or
> military sectors, you need to apply additional measures and may override some roles.

> **WARNING:**
> This role makes use of external repositories for MariaDB (from MariaDB maintainers), Apach2 and PHP (deb.sury.org) as
> well as Nginx (nginx repos) and ISC BIND9 to provide all security relevant patches as well as feature updates.
> This can be disabled via `maintainer_repositories: false`. If you do not define this variable it is handled as `true`.

Some roles focus on basic configuration and hardening which is not configurable.
Where possible we use, aside of apparmor, Systemd unit overrides to secure processes. This adds another layer of security
because Systemd will start processes which already have limited capabilities.

> **NOTE**:
> All roles providing networking services depend on the `nftables` role so no extra firewall frontend is needed.
> Any service providing networking services (such as Nginx, Apache2 or OpenSearch) will provide its own ruleset.

## Dependencies

This role depends on several different Python libraries which do not come with the `ansible` or `ansible-core` packages.
- netaddr

## Default values

For most variables defined in roles we use defaults. Those defaults are defined where they are used.
You will find them in templates and task files next to the variable.
Unfortunately this means one can not rely on these variable values when they are not defined by the user if one wants to
use a variable somewhere else.
However, templates are a lot more readable doing this.
