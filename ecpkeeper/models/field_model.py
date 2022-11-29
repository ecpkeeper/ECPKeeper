class Field:
    def __init__(self, default=None, disabled=False, initial=None, label=None, required=True, values=None):
        self.default = default
        self.disabled = disabled
        self.initial = initial
        self.label = label
        self.required = required
        self.values = values or {}
