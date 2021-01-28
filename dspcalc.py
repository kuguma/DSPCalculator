
recipes = {
    "Small carrier rocket" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Dyson sphere component" : 2,
            "Deutron fuel rod" : 2,
            "Quantum chip" : 2
        }
    },
    "Dyson sphere component" : {
        "fac" : "asm",
        "sec" : 8,
        "components" : {
            "Frame material" : 3,
            "Solar sail" : 3,
            "Processor" : 3
        }
    },
    "Frame material" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Carbon nanotube" : 4,
            "Titanium alloy" : 1,
            "High-purity sillicon" : 1
        }
    },
    "Carbon nanotube" : {
        "fac" : "chem",
        "sec" : 4/2,
        "components" : {
            "Graphene" : 3/2,
            "Titanium ingot" : 1/2,
        }
    },
    "Graphene" : {
        "fac" : "chem",
        "sec" : 3/2,
        "components" : {
            "Energetic graphite" : 3/2,
            "Sulfuric acid" : 1/2,
        }
    },
    "Energetic graphite" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "Coal ore" : 2,
        }
    },
    "Coal ore" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Sulfuric acid" : {
        "fac" : "chem",
        "sec" : 6/4,
        "components" : {
            "Refined oil" : 6/4,
            "Stone ore" : 8/4,
            "Water" : 4/4
        }
    },
    "Refined oil" : {
        "fac" : "chem",
        "sec" : 4/2,
        "components" : {
            "Crude oil" : 2/2,
        }
    },
    "Crude oil" : {
        "fac" : "ref",
        "end" : "seep"
    },
    "Titanium ingot" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "Titanium ore" : 2,
        }
    },
    "Titanium ore" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Titanium alloy" : {
        "fac" : "smelt",
        "sec" : 12/4,
        "components" : {
            "Titanium ingot" : 4/4,
            "Steel" : 4/4,
            "Sulfuric acid" : 8/4
        }
    },
    "Steel" : {
        "fac" : "smelt",
        "sec" : 3,
        "components" : {
            "Iron ingot" : 3/3,
        }
    },
    "Iron ingot" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Solar sail" : {
        "fac" : "asm",
        "sec" : 4/2,
        "components" : {
            "Graphene" : 1/2,
            "Photon combiner" : 1/2,
        }
    },
    "Photon combiner" : {
        "fac" : "asm",
        "sec" : 3,
        "components" : {
            "Prism" : 2,
            "Circuit board" : 1,
        }
    },
    "Prism" : {
        "fac" : "asm",
        "sec" : 2/2,
        "components" : {
            "Glass" : 3/2,
        }
    },
    "Glass" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "Stone ore" : 2,
        }
    },
    "Stone ore" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Circuit board" : {
        "fac" : "asm",
        "sec" : 1/2,
        "components" : {
            "Iron ingot" : 2/2,
            "Copper ingot" : 1/2,
        }
    },
    "Copper ingot" : {
        "fac" : "smelt",
        "sec" : 1,
        "components" : {
            "Copper ore" : 1,
        }
    },
    "Copper ore" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Processor" : {
        "fac" : "asm",
        "sec" : 3,
        "components" : {
            "Circuit board" : 2,
            "Microcrystalline component" : 2,
        }
    },
    "Microcrystalline component" : {
        "fac" : "asm",
        "sec" : 2,
        "components" : {
            "High-purity sillicon" : 2,
            "Copper ingot" : 1,
        }
    },
    "Deutron fuel rod" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Titanium alloy" : 1,
            "Deuterium" : 10,
            "Super-magnetic ring" : 1
        }
    },
    "Deuterium" : {
        "fac" : "part",
        "sec" : 5/5,
        "components" : {
            "Hydrogen" : 10/5,
        }
    },
    "Hydrogen" : {
        "fac" : "orbit",
        "end" : "gas"
    },
    "Super-magnetic ring" : {
        "fac" : "asm",
        "sec" : 3,
        "components" : {
            "Electromagnetic turbine" : 2,
            "Magnet" : 3,
            "Energetic graphite" : 1
        }
    },
    "Magnet" : {
        "fac" : "smelt",
        "sec" : 1.5,
        "components" : {
            "Iron ore" : 1,
        }
    },
    "Iron ore" : {
        "fac" : "mine",
        "end" : "vein"
    },
    "Electromagnetic turbine" : {
        "fac" : "asm",
        "sec" : 2,
        "components" : {
            "Electric motor" : 2,
            "Magnetic coil" : 2,
        }
    },
    "Electric motor" : {
        "fac" : "asm",
        "sec" : 2,
        "components" : {
            "Iron ingot" : 2,
            "Gear" : 1,
            "Magnetic coil" : 1
        }
    },
    "Gear" : {
        "fac" : "asm",
        "sec" : 1,
        "components" : {
            "Iron ingot" : 1,
        }
    },
    "Magnetic coil" : {
        "fac" : "asm",
        "sec" : 1/2,
        "components" : {
            "Magnet" : 2/2,
            "Copper ingot" : 1/2,
        }
    },
    "Quantum chip" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Processor" : 2,
            "Plane filter" : 2,
        }
    },
    "Plane filter" : {
        "fac" : "asm",
        "sec" : 12,
        "components" : {
            "Casimir crystal" : 1,
            "Titanium glass" : 2,
        }
    },
    "Casimir crystal" : {
        "fac" : "asm",
        "sec" : 4,
        "components" : {
            "Titanium crystal" : 1,
            "Graphene" : 2,
            "Hydrogen" : 12
        }
    },
    "Titanium crystal" : {
        "fac" : "asm",
        "sec" : 4,
        "components" : {
            "Organic crystal" : 1,
            "Titanium ingot" : 3,
        }
    },
    "Organic crystal" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Plastic" : 2,
            "Refined oil" : 10,
            "Water" : 1
        }
    },
    "Plastic" : {
        "fac" : "chem",
        "sec" : 3,
        "components" : {
            "Refined oil" : 2,
            "Energetic graphite" : 1,
        }
    },
    "Titanium glass" : {
        "fac" : "asm",
        "sec" : 5,
        "components" : {
            "Glass" : 2,
            "Titanium ingot" : 2,
            "Water" : 2
        }
    },
    "Graviton lens" : {
        "fac" : "asm",
        "sec" : 6,
        "components" : {
            "Diamond" : 4,
            "Strange matter" : 1,
        }
    },
    "Diamond" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "Energetic graphite" : 1,
        }
    },
    "Strange matter" : {
        "fac" : "part",
        "sec" : 8,
        "components" : {
            "Particle container" : 2,
            "Iron ingot" : 2,
            "Hydrogen" : 10
        }
    },
    "Particle container" : {
        "fac" : "asm",
        "sec" : 4,
        "components" : {
            "Electromagnetic turbine" : 2,
            "Copper ingot" : 2,
            "Graphene" : 2
        }
    },
    "Gravity matrix" : {
        "fac" : "res",
        "sec" : 24/2,
        "components" : {
            "Graviton lens" : 1/2,
            "Quantum chip" : 1/2,
        }
    },
    "Information matrix" : {
        "fac" : "res",
        "sec" : 10,
        "components" : {
            "Processor" : 2,
            "Particle broadband" : 1,
        }
    },
    "Particle broadband" : {
        "fac" : "asm",
        "sec" : 8,
        "components" : {
            "Carbon nanotube" : 2,
            "Crystal sillicon" : 2,
            "Plastic" : 1
        }
    },
    "Crystal sillicon" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "High-purity sillicon" : 1,
        }
    },
    "Structure matrix" : {
        "fac" : "res",
        "sec" : 8,
        "components" : {
            "Diamond" : 1,
            "Titanium Crystal" : 1,
        }
    },
    "Energy matrix" : {
        "fac" : "res",
        "sec" : 6,
        "components" : {
            "Energetic graphite" : 2,
            "Hydrogen" : 2,
        }
    },
    "Electromagnetic matrix" : {
        "fac" : "res",
        "sec" : 3,
        "components" : {
            "Magnetic coil" : 1,
            "Circuit board" : 1,
        }
    },
    "Water" : {
        "fac" : "pump",
        "end" : "pump"
    },
    "High-purity sillicon" : {
        "fac" : "smelt",
        "sec" : 2,
        "components" : {
            "Sillicon ore" : 2,
        }
    },
    "Sillicon ore" : {
        "fac" : "mine",
        "end" : "vein"
    },

}

# 
ignore_list = ["Processor"]

def search_recipe(name, pcs, result):
    if name in recipes:
        entry = recipes[name]
        if name not in result:
            result[name] = 0
        result[name] += pcs
        if "end" in entry or name in ignore_list:
            return
        else:
            for k, i in entry["components"].items():
                search_recipe(k, pcs*i, result)
            return
    print(f"!!! no data : {name}")

from collections import OrderedDict

def main():
    print("< Dyson Sphere Program - calculator >\n")
    # req = "Gravity_matrix"
    req = input("Enter the name of component > ")
    result = dict()
    search_recipe(req, 1, result)
    result = OrderedDict(sorted(result.items(), key=lambda x:x[1]))
    print(f"| {'[ Name ]':^28} | {'pcs':>6} | {'fac':^5} | N ")
    for name, pcs in result.items():
        e = recipes[name]
        fac = e["fac"]
        if "sec" in e:
            n = pcs * e["sec"]
        else:
            n = '-'
        print(f"| {name:^28} | {pcs:>6.2f} | {fac:^5} | {n}")






if __name__=='__main__':
    main()

