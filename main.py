def total_aberration(R, n_lambda1, n_lambda2, r, M, u):
    """
    Calculate the total aberration Δx_total.

    Parameters:
    R (float): Radius of curvature of the lens.
    n_lambda1 (float): Refractive index for wavelength λ1.
    n_lambda2 (float): Refractive index for wavelength λ2.
    r (float): Aperture radius of the lens.
    M (float): Magnification of the lens.
    u (float): Object distance from the lens.

    Returns:
    float: Total aberration Δx_total.
    """
    # Calculate the first term
    term1 = R * (1 / (n_lambda2 - 1) - 1 / (n_lambda1 - 1))

    # Calculate the second term
    term2 = (r**2) / (8 * (1 + 1/M)**2 * u**2)

    # Total aberration
    delta_x_total = term1 + term2

    return delta_x_total

# Example usage:
R = 10.0      # Example value for the radius of curvature
n_lambda1 = 1.5  # Example refractive index for λ1
n_lambda2 = 1.52  # Example refractive index for λ2
r = 5.0        # Example value for the aperture radius
M = 2.0        # Example magnification
u = 100.0      # Example object distance

# Calculate total aberration
delta_x = total_aberration(R, n_lambda1, n_lambda2, r, M, u)
print("Total Aberration Δx_total:", delta_x)
