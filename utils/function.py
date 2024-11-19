def redor_bessel(max_order):
    from scipy.special import jv

    def calculator(t, d_IS):
        if max_order > 5:
            pass  # for raising error

        z = t * 2**0.5 * d_IS

        redor_predict = 1 - jv(0, z)**2

        for order in range(1,max_order):
            redor_predict = redor_predict + 2 / (16*order**2-1) * jv(order, z)**2
    
        return redor_predict
    return calculator


def ctdrenar():
    from numpy import cos
    from scipy.constants import pi

    def calculator(theta, z):
        return 6/5 * z * (1+cos(2*theta*pi/180))  # z = (d*t)^2
    return calculator


def drenar_parabola():
    from scipy.constants import pi

    def calculator(t, d):
        return 0.86*pi*pi/15*d*d*t*t
    return calculator


def redor_threehalf():
    from scipy.special import jv
    from scipy.constants import pi

    def calculator(t, d_IS):

        z = t * 2**0.5 * d_IS

        redor_predict = 1 - 2**0.5 * pi / 8 * (jv(0.25, z)*jv(-0.25, z)+jv(0.25, 3*z)*jv(-0.25, 3*z))
    
        return redor_predict
    return calculator


def reapdor_threehalf():
    from numpy import exp

    def calculator(t, d_IS):

        redor_predict = 0.75 - 0.75*exp(-(1.75*t*d_IS)**2)
    
        return redor_predict
    return calculator


def reapdor_PB_natural_abundance():
    from numpy import exp

    def calculator(t, r_IS):

        redor_predict = 0.60 - 0.60*exp(-(27.2*t)**2*r_IS**(-6))
    
        return redor_predict
    return calculator


def expdec(t, a, b, R):
    from numpy import exp

    return a + b*exp(-R*t)


def satrec(t, a, b, R):
    from numpy import exp

    return a - b*exp(-R*t)