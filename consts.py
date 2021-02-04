recipes = {
    "Small carrier rocket": {
        "fac": "asm",
        "sec": 6,
        "components": {"Dyson sphere component": 2, "Deuteron fuel rod": 2, "Quantum chip": 2},
    },
    "Dyson sphere component": {
        "fac": "asm",
        "sec": 8,
        "components": {"Frame material": 3, "Solar sail": 3, "Processor": 3},
    },
    "Frame material": {
        "fac": "asm",
        "sec": 6,
        "components": {"Carbon nanotube": 4, "Titanium alloy": 1, "High-purity silicon": 1},
    },
    "Carbon nanotube": {
        "fac": "chem",
        "sec": 4 / 2,
        "components": {
            "Graphene": 3 / 2,
            "Titanium ingot": 1 / 2,
        },
    },
    "Graphene": {
        "fac": "chem",
        "sec": 3 / 2,
        "components": {
            "Energetic graphite": 3 / 2,
            "Sulfuric acid": 1 / 2,
        },
    },
    "Energetic graphite": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "Coal ore": 2,
        },
    },
    "Coal ore": {"fac": "mine", "end": "vein"},
    "Sulfuric acid": {
        "fac": "chem",
        "sec": 6 / 4,
        "components": {"Refined oil": 6 / 4, "Stone ore": 8 / 4, "Water": 4 / 4},
    },
    "Refined oil": {
        "fac": "ref",
        "sec": 4 / 2,
        "components": {
            "Crude oil": 2 / 2,
        },
    },
    "Crude oil": {"fac": "ext", "end": "seep"},
    "Titanium ingot": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "Titanium ore": 2,
        },
    },
    "Titanium ore": {"fac": "mine", "end": "vein"},
    "Titanium alloy": {
        "fac": "smelt",
        "sec": 12 / 4,
        "components": {"Titanium ingot": 4 / 4, "Steel": 4 / 4, "Sulfuric acid": 8 / 4},
    },
    "Steel": {
        "fac": "smelt",
        "sec": 3,
        "components": {
            "Iron ingot": 3,
        },
    },
    "Iron ingot": {"fac": "smelt", "sec": 1, "components": {"Iron ore": 1}},
    "Solar sail": {
        "fac": "asm",
        "sec": 4 / 2,
        "components": {
            "Graphene": 1 / 2,
            "Photon combiner": 1 / 2,
        },
    },
    "Photon combiner": {
        "fac": "asm",
        "sec": 3,
        "components": {
            "Prism": 2,
            "Circuit board": 1,
        },
    },
    "Prism": {
        "fac": "asm",
        "sec": 2 / 2,
        "components": {
            "Glass": 3 / 2,
        },
    },
    "Glass": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "Stone ore": 2,
        },
    },
    "Stone ore": {"fac": "mine", "end": "vein"},
    "Circuit board": {
        "fac": "asm",
        "sec": 1 / 2,
        "components": {
            "Iron ingot": 2 / 2,
            "Copper ingot": 1 / 2,
        },
    },
    "Copper ingot": {
        "fac": "smelt",
        "sec": 1,
        "components": {
            "Copper ore": 1,
        },
    },
    "Copper ore": {"fac": "mine", "end": "vein"},
    "Processor": {
        "fac": "asm",
        "sec": 3,
        "components": {
            "Circuit board": 2,
            "Microcrystalline component": 2,
        },
    },
    "Microcrystalline component": {
        "fac": "asm",
        "sec": 2,
        "components": {
            "High-purity silicon": 2,
            "Copper ingot": 1,
        },
    },
    "Deuteron fuel rod": {
        "fac": "asm",
        "sec": 6,
        "components": {"Titanium alloy": 1, "Deuterium": 10, "Super-magnetic ring": 1},
    },
    "Deuterium": {
        "fac": "part",
        "sec": 5 / 5,
        "components": {
            "Hydrogen": 10 / 5,
        },
    },
    "Hydrogen": {"fac": "orbit", "end": "gas"},
    "Super-magnetic ring": {
        "fac": "asm",
        "sec": 3,
        "components": {"Electromagnetic turbine": 2, "Magnet": 3, "Energetic graphite": 1},
    },
    "Magnet": {
        "fac": "smelt",
        "sec": 1.5,
        "components": {
            "Iron ore": 1,
        },
    },
    "Iron ore": {"fac": "mine", "end": "vein"},
    "Electromagnetic turbine": {
        "fac": "asm",
        "sec": 2,
        "components": {
            "Electric motor": 2,
            "Magnetic coil": 2,
        },
    },
    "Electric motor": {"fac": "asm", "sec": 2, "components": {"Iron ingot": 2, "Gear": 1, "Magnetic coil": 1}},
    "Gear": {
        "fac": "asm",
        "sec": 1,
        "components": {
            "Iron ingot": 1,
        },
    },
    "Magnetic coil": {
        "fac": "asm",
        "sec": 1 / 2,
        "components": {
            "Magnet": 2 / 2,
            "Copper ingot": 1 / 2,
        },
    },
    "Quantum chip": {
        "fac": "asm",
        "sec": 6,
        "components": {
            "Processor": 2,
            "Plane filter": 2,
        },
    },
    "Plane filter": {
        "fac": "asm",
        "sec": 12,
        "components": {
            "Casimir crystal": 1,
            "Titanium glass": 2,
        },
    },
    "Casimir crystal": {"fac": "asm", "sec": 4, "components": {"Titanium crystal": 1, "Graphene": 2, "Hydrogen": 12}},
    "Titanium crystal": {
        "fac": "asm",
        "sec": 4,
        "components": {
            "Organic crystal": 1,
            "Titanium ingot": 3,
        },
    },
    "Organic crystal": {"fac": "asm", "sec": 6, "components": {"Plastic": 2, "Refined oil": 10, "Water": 1}},
    "Plastic": {
        "fac": "chem",
        "sec": 3,
        "components": {
            "Refined oil": 2,
            "Energetic graphite": 1,
        },
    },
    "Titanium glass": {
        "fac": "asm",
        "sec": 5 / 2,
        "components": {"Glass": 2 / 2, "Titanium ingot": 2 / 2, "Water": 2 / 2},
    },
    "Graviton lens": {
        "fac": "asm",
        "sec": 6,
        "components": {
            "Diamond": 4,
            "Strange matter": 1,
        },
    },
    "Diamond": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "Energetic graphite": 1,
        },
    },
    "Strange matter": {
        "fac": "part",
        "sec": 8,
        "components": {"Particle container": 2, "Iron ingot": 2, "Hydrogen": 10},
    },
    "Particle container": {
        "fac": "asm",
        "sec": 4,
        "components": {"Electromagnetic turbine": 2, "Copper ingot": 2, "Graphene": 2},
    },
    "Gravity matrix": {
        "fac": "res",
        "sec": 24 / 2,
        "components": {
            "Graviton lens": 1 / 2,
            "Quantum chip": 1 / 2,
        },
    },
    "Information matrix": {
        "fac": "res",
        "sec": 10,
        "components": {
            "Processor": 2,
            "Particle broadband": 1,
        },
    },
    "Particle broadband": {
        "fac": "asm",
        "sec": 8,
        "components": {"Carbon nanotube": 2, "Crystal silicon": 2, "Plastic": 1},
    },
    "Crystal silicon": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "High-purity silicon": 1,
        },
    },
    "Structure matrix": {
        "fac": "res",
        "sec": 8,
        "components": {
            "Diamond": 1,
            "Titanium Crystal": 1,
        },
    },
    "Energy matrix": {
        "fac": "res",
        "sec": 6,
        "components": {
            "Energetic graphite": 2,
            "Hydrogen": 2,
        },
    },
    "Electromagnetic matrix": {
        "fac": "res",
        "sec": 3,
        "components": {
            "Magnetic coil": 1,
            "Circuit board": 1,
        },
    },
    "Water": {"fac": "pump", "end": "pump"},
    "High-purity silicon": {
        "fac": "smelt",
        "sec": 2,
        "components": {
            "Silicon ore": 2,
        },
    },
    "Silicon ore": {"fac": "mine", "end": "vein"},
    "Accumulator": {
        "fac": "asm",
        "sec": 5,
        "components": {"Iron ingot": 6, "Super-magnetic ring": 6, "Crystal silicon": 4},
    },
    "Planetary Logistics Station": {
        "fac": "asm",
        "sec": 20,
        "components": {"Steel": 40, "Titanium ingot": 40, "Processor": 40, "Particle container": 20},
    },
    "Intersteller Logistics Station": {
        "fac": "asm",
        "sec": 30,
        "components": {"Planetary Logistics Station": 1, "Titanium alloy": 40, "Particle container": 20},
    },
    "Orbit collector": {
        "fac": "asm",
        "sec": 30,
        "components": {
            "Intersteller Logistics Station": 1,
            "Super-magnetic ring": 50,
            "Reinforced thruster": 20,
            "Accumulator": 20,
        },
    },
    "Reinforced thruster": {
        "fac": "asm",
        "sec": 6,
        "components": {
            "Titanium alloy": 5,
            "Super-magnetic ring": 5,
        },
    },
    "Annihilation constraint sphere": {
        "fac": "asm",
        "sec": 20,
        "components": {
            "Particle container": 1,
            "Processor": 1,
        },
    },
    "Antimatter fuel rod": {
        "fac": "asm",
        "sec": 12,
        "components": {"Antimatter": 10, "Hydrogen": 10, "Annihilation constraint sphere": 1, "Titanium alloy": 1},
    },
    "Spiniform stalagmite crystal": {"fac": "mine", "end": "vein"},
    "Fire ice": {"fac": "mine", "end": "vein"},
}

advanced_recipes = {
    "Graphene": {
        "fac": "chem",
        "sec": 2 / 2,
        "components": {
            "Fire ice": 2 / 2,
        },
    },
    "Carbon nanotube": {
        "fac": "chem",
        "sec": 4 / 2,
        "components": {
            "Spiniform stalagmite crystal": 2 / 2,
        },
    },
    "Sulfuric acid": {"fac": "pump", "end": "pump"},
    "Organic crystal": {"fac": "mine", "end": "vein"},
    "Deuterium": {"fac": "orbit", "end": "gas"},
}

facilities = {
    "asm": {"work": 480, "idle": 15},
    "smelt": {"work": 360, "idle": 12},
    "ref": {"work": 960, "idle": 24},
    "chem": {"work": 720, "idle": 24},
    "part": {"work": 12000, "idle": 120},
    "ext": {"work": 840, "idle": 24, "speed": 2.0},  # 2.0/s
    "pump": {"work": 300, "idle": 12, "speed": 1},  # 1.0/s
    "mine": {"work": 420, "idle": 24, "speed": 0.5 * 5},  # 5 vein
    "res": {"work": 480, "idle": 12},
    "orbit": {"work": 0, "idle": 0, "speed": 0.87 * 12 - (30 / 8)},
}

ignore_list = ["Processor", "Sulfuric acid"]
