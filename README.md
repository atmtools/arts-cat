# arts-cat
The steps required to generate Artscat, the absorption line catalog of ARTS

This is the software used to generate Artscat, which is available as supporting data to ARTS (www.github.com/atmtools/arts)

The intent of this project is to curate Artscat and to continuously provide updates to various parameters within it.

# Usage

python arts-cat.py path/to/hitran-file

Use --help to see more options.

# Recipies

The current recipies are

1) ReadHitran --- Reads Hitran data base (hitran.org) and generates a basic set of data.  Reference: I. Gordon, L. Rothman, R. Hargreaves et al. (2021), "The HITRAN2020 molecular spectroscopic database", Journal of Quantitative Spectroscopy and Radiative Transfer, 107949, [doi.org/10.1016/j.jqsrt.2021.107949](https://doi.org/10.1016/j.jqsrt.2021.107949).

2) Water183 --- Replaces the 183 GHz absorption line with one of our own.  Reference: O. Bobryshev, S.A. Buehler, V.O. John, M. Brath, and H. Brogniez (2018), Is There Really a Closure Gap Between 183.31-GHz Satellite Passive Microwave and In Situ Radiosonde Water Vapor Measurements?, IEEE Transaction On Geoscience And Remote Sensing, 56(5), 2904-2910, [doi:10.1109/TGRS.2017.2786548](http://dx.doi.org/10.1109/TGRS.2017.2786548).

3) Zeeman --- Replace Zeeman coefficients with pre-computed coefficients.  References: R. Larsson, B. Lankhaar, and P. Eriksson (2019), Updated Zeeman effect splitting coefficients for molecular oxygen in planetary applications, Journal of Quantitative Spectroscopy and Radiative Transfer, 224, 431-438, [doi.org/10.1016/j.jqsrt.2018.12.004](https://doi.org/10.1016/j.jqsrt.2018.12.004) AND R. Larsson and B. Lankhaar (2020), Zeeman effect splitting coefficients for ClO, OH and NO in some earth atmosphere applications, Journal of Quantitative Spectroscopy and Radiative Transfer, 250, 107050, [doi.org/10.1016/j.jqsrt.2020.107050](https://doi.org/10.1016/j.jqsrt.2020.107050).

4) OxygenLM --- Set line mixing of the 60 GHz ground-state lines of O2-66 by own calculations.  Reference: D.S. Makarov, M.Y. Tretyakov, and P.W. Rosenkranz (2020), Revision of the 60-GHz atmospheric oxygen absorption band models for practical use, 243, 106098, [doi.org/10.1016/j.jqsrt.2019.106798](https://doi.org/10.1016/j.jqsrt.2019.106798).

