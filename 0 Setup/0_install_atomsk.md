# Install [atomsk](https://atomsk.univ-lille.fr)

## Steps

    1. Download atomsk from [HERE](https://atomsk.univ-lille.fr/dl.php). I use git clone the repo from the website.
    ```sys
        git clone https://github.com/pierrehirel/atomsk/
    ```

    2. As the download website suggested, enter the following codes to build.
    ```sys
        cd src
    ```

Before making the build, check if gfortran is installed. If not, it can be downloaded from [HERE](https://gcc.gnu.org/wiki/GFortranBinaries). After properly install gfortran, run the following code in terminal.

    ```sys
        make atomsk
    ```
