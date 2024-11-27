import numpy as np

def calculate_chromatic_aberration(R, n_lambda1, n_lambda2):
    """
    Calculate chromatic aberration.
    Args:
        R: Radius of curvature of the lens (mm or any consistent unit).
        n_lambda1: Refractive index for wavelength lambda1.
        n_lambda2: Refractive index for wavelength lambda2.
    Returns:
        Chromatic aberration in the same units as R.
    """
    return R * (1 / (n_lambda2 - 1) - 1 / (n_lambda1 - 1))

def calculate_spherical_aberration(r, f):
    """
    Calculate spherical aberration.
    Args:
        r: Radius of the lens (mm or any consistent unit).
        f: Focal length of the lens (same unit as r).
    Returns:
        Spherical aberration in the same units as r and f.
    """
    return (r**2) / (8 * f**2)

def calculate_total_aberration(chromatic_aberration, spherical_aberration):
    """
    Calculate total aberration as the sum of chromatic and spherical aberration.
    Args:
        chromatic_aberration: Chromatic aberration value.
        spherical_aberration: Spherical aberration value.
    Returns:
        Total aberration.
    """
    return chromatic_aberration + spherical_aberration

# Example inputs
R = 100  # Radius of curvature of the lens (mm)
n_lambda1 = 1.50  # Refractive index for wavelength lambda1 (e.g., red)
n_lambda2 = 1.55  # Refractive index for wavelength lambda2 (e.g., blue)
r = 50  # Radius of the lens (mm)
f = 200  # Focal length of the lens (mm)

# Calculations
chromatic_aberration = calculate_chromatic_aberration(R, n_lambda1, n_lambda2)
spherical_aberration = calculate_spherical_aberration(r, f)
total_aberration = calculate_total_aberration(chromatic_aberration, spherical_aberration)

# Output
print(f"Chromatic Aberration: {chromatic_aberration:.4f} mm")
print(f"Spherical Aberration: {spherical_aberration:.4f} mm")
print(f"Total Aberration: {total_aberration:.4f} mm")
