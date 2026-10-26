import yaml


def load_rules(path: str):
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def apply_rules(view_data, rules_path: str):
    rules = load_rules(rules_path)
    print("Applying enterprise rules")
    return {"views": view_data["views"], "rules": rules}
