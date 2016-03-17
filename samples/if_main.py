import if_sample
import collections

locales = collections.OrderedDict(house=['north','look'],
                                  hill=['east','light'])

path = []
for locale in locales:
    path.append(if_sample.Location(locale, locales[locale]))

print(path)

