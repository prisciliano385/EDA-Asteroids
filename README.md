# EDA-Asteroids

 This *Exploratory Data Analysis* analyzes a dataset containg information on more than $10^5$ asteroids in the Solar System. The Solar System is full of small bodies, with sizes that range from a few meters to the almost $10^3\,km$ wide Ceres (although it is no longer considered a small body). Their composition varies greatly, from the *icy* outer asteroids from the Kuiper belt to the more *rocky* of the main belt.
 
 In addition to orbital parameters, such as the semi-major axis, orbital period, perihelium and aphelium distances and their uncertainties, brightness related parameters, such as the absolute magnitude and the albedo are included. In addition, asteroids are classified into different groups, depending on their orbital parameters. The risk that each asteroids means for us is also specified on the file. Let's get into depth!

## Hypothesis:
1- Initial analysis of the dataset:
    - What are the ranges of semi-major axis and eccentricity (a measure of an orbit's non-circularity)?
    - How many asteroids have an eccentricity bigger than 1? Orbits with eccentricity values in the range $0 < e < 1$ are bound orbits, whilst those with values $e > 1$ are parabolic or hyperbolic, meaning that they will leave the Solar System in the future.

2- Main characteristics vs Asteroid classification:
    - One of the most extended asteroid classification criteria (and the one used in the dataset) is based on orbital parameters. Check how the **semi-major axis** and **orbital period** varies between different asteroid groups.
    - Check how different groups of asteroids have different values of **eccentricity** (a measure of an orbit's non-circularity).
    - Check how different groups of asteroids have different values of the inclination (the angle between the ecliptic plane and the orbit plane).
    - Check the absolute magnitude ($H$) is distributed between different asteroid groups.
