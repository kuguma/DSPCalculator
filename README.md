# DSPCalculator
The Calculator for Dyson Sphere Program (game).

This is CLI tool.

## Sample

```shell

$ > python '.\dspcalc.py'
< Dyson Sphere Program - calculator >

Enter the name of component > Information matrix
|           [ Name ]           |    pcs |  fac  | N
|      Information matrix      |   1.00 |  res  | 10
|      Particle broadband      |   1.00 |  asm  | 8
|        Titanium ingot        |   1.00 | smelt | 2.0
|           Plastic            |   1.00 | chem  | 3
|        Sulfuric acid         |   1.50 | chem  | 2.25
|            Water             |   1.50 | pump  | -
|          Processor           |   2.00 |  asm  | 6
|       Carbon nanotube        |   2.00 | chem  | 4.0
|         Titanium ore         |   2.00 | mine  | -
|       Crystal sillicon       |   2.00 | smelt | 4
|     High-purity sillicon     |   2.00 | smelt | 4
|           Graphene           |   3.00 | chem  | 4.5
|          Stone ore           |   3.00 | mine  | -
|         Sillicon ore         |   4.00 | mine  | -
|         Refined oil          |   4.25 | chem  | 8.5
|          Crude oil           |   4.25 |  ref  | -
|      Energetic graphite      |   5.50 | smelt | 11.0
|           Coal ore           |  11.00 | mine  | -

```

## Try it

```shell
python3 dspcalc.py
```

## Features

- When you enter the name of the component, it outputs the required material and the number of factories needed to produce deliverable at 1pcs/s.
