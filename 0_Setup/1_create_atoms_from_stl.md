# Create atoms from .stl

I follow [Tutorial: Select Atoms According to a 3-D Shape](https://atomsk.univ-lille.fr/tutorial_STL.php) steps from scratch.

## Fiber Reinforced Polymer (FRP)

1. Here I prepared matrix.stl and fiber.stl.

   * matrix:
       ![alt text](/0_Setup/source/matrix.png)
   * fiber:
       ![alt text](/0_Setup/source/fiber.png)

2. Change current directory.

    ```sys
    cd 0_Setup
    ```

3. Create a file full of Al atoms.

    ```sys
    atomsk --create fcc 4.046 Al -duplicate 40 40 40 Al_supercell.xsf
    ```

4. Select the stl and remove other atoms.

    ```sys
    atomsk Al_supercell.xsf -select stl center matrix.stl -select invert -rmatom select MD-matrix.xsf
    ```

   * `Al_supercell.xsf` opens the file full of Al atoms.
   * `-select stl [center] matrix.stl` opens matrix.stl and put it into the center, atomsk will atomatically resize the .stl to the input file.
   * `-select invert` selects inversion of the matrix (i.e., fiber).
   * `-rmatom` removes the atoms within the selection.
   * `select MD-matrix.xsf` saves the result to fiber.xsf.

   * Following is the result of matrix model
   ![alt text](/0_Setup/MD-matrix.png)

5. Likewise, create MD-fiber by removing inversion of what inside of fiber.stl

Note: there seems to be problem reading .stl within other folder, so make sure .stl is put right in the `cd` folder ~~./source/~~.

```sys
atomsk Al_supercell.xsf -select stl center ./source/fiber.stl -select invert  -rmatom select MD-fiber.xsf
```

![alt text](/0_Setup/MD-fiber.png)
