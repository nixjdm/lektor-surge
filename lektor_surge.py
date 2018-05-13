# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.publisher import Publisher, Command


class SurgePublisher(Publisher):
    def publish(self, target_url, credentials=None, **extra):
        if target_url.scheme == 'surge+https':
            url = 'https://' + target_url.path
        else:
            url = target_url.path

        for line in Command(['surge', '-p', self.output_path, url]):
            yield line


class SurgePlugin(Plugin):
    name = u'Surge'
    description = u'Lektor plugin to publish your site to surge.sh'

    def on_setup_env(self, **extra):
        for scheme in ('surge', 'surge+https'):
            try:
                # Lektor 2.0+.
                self.env.add_publisher(scheme, SurgePublisher)
            except AttributeError:
                # Lektor 1.0.
                from lektor.publisher import publishers
                publishers[scheme] = SurgePublisher
