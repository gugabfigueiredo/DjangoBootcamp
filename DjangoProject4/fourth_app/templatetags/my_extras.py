# -*- coding: utf-8 -*-
import re

from django import template


register = template.Library()


@register.filter(name='trim')
def trim(string, cut):

    '''
    Trims out chars or substrings from a string.

    string is a seed string from which chars and substrings will be cut.

    Chars and substrings to be trimmend can be directly referenced as named parameters. If
    specified, subs must be a list of substrings and chars can be either a list of characters
    or a string, which will be treated as a list of characters.

    Chars and substrings can also be passed as a list of parameters. In this case, they are
    treated as substrings and are trimmed in the order they are passed in.

    If specified, spacing dictates what kind of spacing is used as seprator for trimming.
    It can be one of 'simple', 'sparse' or None. If spacing is simple, trim will result
    in a single whitespace between remaining characters in the string. If spacing is sparce,
    every character removed will result in a whitesapce in the resulting string. If spacing
    is None, no spacing will be done.

    '''

    #chars = kwargs.get('chars', '')
    #subs = kwargs.get('subs', list(args))

    #cuts = subs + list(chars)

    #spacing = kwargs.get('spacing', None)

    #sep = ''

    #if spacing:

        #sep = ' '

    #for cut in cuts:

        #string = string.replace(cut, sep * len(cut))

    #if spacing == 'simple':

        #string = re.sub(' +', ' ', string)

    return string.replace(cut, '').strip()

    #return string.strip()


#register.filter('trim', trim)
