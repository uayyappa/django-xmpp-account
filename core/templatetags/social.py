# -*- coding: utf-8 -*-
# vim: expandtab:tabstop=4:hlsearch
#
# This file is part of django-xmpp-account (https://github.com/mathiasertl/django-xmpp-account/).
#
# django-xmpp-account is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# django-xmpp-account is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-xmpp-account.
# If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from django import template

register = template.Library()


@register.inclusion_tag("core/social.html", takes_context=True)
def social(context, noauto=False):
    context = {
        'SITE': context['SITE'],
        'noauto': noauto,
    }
    if context['SITE'].get('FACEBOOK'):
        context['FACEBOOK_URL'] = 'https://www.facebook.com/%s' % context['SITE']['FACEBOOK']
    return context