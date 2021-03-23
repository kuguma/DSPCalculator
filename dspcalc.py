from collections import OrderedDict

from consts import (
    recipes,
    advanced_recipes,
    facilities,
    ignore_list,
)


def setup_advanced_recipe():
    advanced_materials = [
        "Carbon nanotube",
        "Graphene",
        "Sulfuric acid",
        "Organic crystal",
        # "Deuterium"
    ]
    for material in advanced_materials:
        recipes[material] = advanced_recipes[material]


def search_recipe(name, pcs, result, parent):
    if name in recipes:
        entry = recipes[name]
        if name not in result:
            result[name] = dict()
            result[name]["pcs"] = 0
            result[name]["dest"] = set()
        result[name]["pcs"] += pcs
        result[name]["dest"].add(parent)
        if "end" in entry or name in ignore_list:
            return
        else:
            for k, i in entry["components"].items():
                search_recipe(k, pcs * i, result, name)
            return
    print(f"!!! no data : {name}")


def is_depend_on(parent_name, child_name):
    result = dict()
    search_recipe(parent_name, 1, result, "")
    return child_name in result


def get_component_name():
    req = input("Enter the name of component > ")
    return req


def add_depend_row(name):
    dep = ""
    children = [
        "Iron ore",
        "Copper ore",
        "Titanium ore",
        "Silicon ore",
        "Stone ore",
        "Coal ore",
        "Crude oil",
        "Hydrogen",
    ]
    for child in children:
        if is_depend_on(name, child):
            dep += "x | "
        else:
            dep += "  | "
    return dep


def main():
    setup_advanced_recipe()
    print("[ Dyson Sphere Program - calculator ]\n")
    req = get_component_name()
    req = req.split(",")
    req_name = req[0]
    req_pcs = 1 if len(req) != 2 else float(req[1])
    print(req)
    result = dict()
    search_recipe(req_name, req_pcs, result, "")
    result = OrderedDict(sorted(result.items(), key=lambda x: x[1]["pcs"]))

    gen_speed = 1 / 6
    print(f"(Target Production speed = {gen_speed:1.2f} pcs/s)")

    print(f"| {'[ Name ]':^28} | {'pcs':>6} | {'fac':^5} | {'N':^5} ||Fe |Cu |Ti |Si |st |co |oi | H || ->")
    consumption = 0
    for name, d in result.items():
        e = recipes[name]
        fac = e["fac"]
        pcs = d["pcs"]
        if "sec" in e:
            n = pcs * e["sec"] * gen_speed
            consumption += e["sec"] * facilities[fac]["work"] * pcs
        else:
            n = pcs * 1 / facilities[fac]["speed"] * gen_speed
        dep = add_depend_row(name)
        dest = d["dest"]
        print(f"| {name:^28} | {pcs:>6.2f} | {fac:^5} | {n:>5.2f} || {dep} || {dest}")

    print(f"[ consumption ] {consumption/1000} MJ / pcs = {consumption/1000*gen_speed} MW / s")


if __name__ == "__main__":
    main()
