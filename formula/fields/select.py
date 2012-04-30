from field import Field

class Select(Field):
    """Class for a select field."""
    def __init__(self, name, options, size=1, **kwargs):
        self.options = options
        self.size = size
        Field.__init__(self, name, **kwargs)

    def __html__(self):
        r = ['<select name="', self.name, '" id="']
        if self.parent_name:
            r.extend([self.parent_name, '_'])
        r.extend([self.name, '" size="', str(self.size), '">'])

        for option in self.options:
            r.extend(['<option value="', self.escape(option), '"'])
            #If it's a dictionary, get the text, otherwise use the value
            if isinstance(self.options, dict):
                if str(self.options[option])==self.value:
                    r.append(' selected="selected"')
                r.append('>')
                r.append(self.escape(self.options[option]))
            else:
                if str(option)==self.value:
                    r.append(' selected="selected"')
                r.append('>')
                r.append(self.escape(option))
            r.append('</option>')

        r.append('</select>')
        return self.renderer(self, ''.join(r))

