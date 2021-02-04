from consts import (
    recipes,
    advanced_recipes,
    facilities,
    ignore_list,
)


def use_advanced_recipe(name):
    recipes[name] = advanced_recipes[name]


use_advanced_recipe("Carbon nanotube")
use_advanced_recipe("Graphene")
use_advanced_recipe("Sulfuric acid")
use_advanced_recipe("Organic crystal")
# use_advanced_recipe("Deuterium")


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
                search_recipe(k, pcs*i, result, name)
            return
    print(f"!!! no data : {name}")


def depend(parent_name, child_name):
    result = dict()
    search_recipe(parent_name, 1, result, "")
    return (child_name in result)

from collections import OrderedDict

def main():
    print("[ Dyson Sphere Program - calculator ]\n")
    req = input("Enter the name of component > ").split(",")
    req_name = req[0]
    req_pcs = 1 if len(req) != 2 else float(req[1])
    print(req)
    result = dict()
    search_recipe(req_name, req_pcs, result, "")
    result = OrderedDict(sorted(result.items(), key=lambda x:x[1]["pcs"]))

    gen_speed = 1/6
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
        
        def depend_str(child_name):
            return "x" if depend(name, child_name) else " "

        dep = ""
        dep += depend_str("Iron ore") + " | "
        dep += depend_str("Copper ore") + " | "
        dep += depend_str("Titanium ore") + " | "
        dep += depend_str("Silicon ore") + " | "
        dep += depend_str("Stone ore") + " | "
        dep += depend_str("Coal ore") + " | "
        dep += depend_str("Crude oil") + " | "
        dep += depend_str("Hydrogen")
        
        dest = d["dest"]
        print(f"| {name:^28} | {pcs:>6.2f} | {fac:^5} | {n:>5.2f} || {dep} || {dest}")
    
    print(f"[ consumption ] {consumption/1000} MJ / pcs = {consumption/1000*gen_speed} MW / s")


if __name__ == '__main__':
    main()

