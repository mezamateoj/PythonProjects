#rom BasicFinance import adc
import datetime

today = datetime.date.today()
maturity = datetime.date(2023, 5, 15)


def annuity_payments(r, n):
    first = 1 / r
    second = 1 / (r * (1 + r)**n)
    return first - second

def zero_c(f, r, t):
    """Zero Coupun bond
        f: face value
        r: discount rate
        t: maturity"""
    r = r / 100
    return f / (1 + r)**t

# what if we know the market value and principal - not r
# solve to r, irr or yield to maturity of bond

def yield_to_m(face_value, market_value, t):
    """yield to maturity"""
    return (face_value / market_value) ** (1 / t) - 1

def effective_annual_r(r, d):
    """Effective annual rate
        r: APR
        d: days to maturity"""
    r = r / 100
    effective = (1 + r) ** (360 / d) - 1
    return effective

# Yield to Maturity = [Annual Interest + {(FV-Price)/Maturity}] / [(FV+Price)/2]
def ytm_coupon(cr, mktprice, fv, n, period):
    coupon = ((cr/100) * fv) / period
    print(coupon)
    y = (coupon + ((fv - mktprice) / n)) / ((fv + mktprice) / 2) 
    return y

# coupon bonds 
def coupon_bond(cr, r, period, principal, n):
    """Coupon bonds value
    cr: coupon rate
    r: discount rate - interest rate
    period: semi, annualy quarterly
    principal: face value
    n: year to maturity of bond"""
    r = r / 100
    cr = cr / 100
    periods = period * n
    coupon = (cr * principal) / period
    r = r / period
    present_value = coupon * annuity_payments(r, periods)
    face_value_discount = principal / (1 + r) ** periods
    return present_value + face_value_discount


def treasury_bill(fv, dq, n):
    """T-bill price
        fv: face value.
        dq: discount quote %.
        n: days to maturity."""
    dq = dq / 100
    pv = fv * (1 - dq * (n / 360))
    return pv

# We annualize this rate of return to express it as a yield to maturity
def t_bill_irr(price, fv):
    return (fv / price) - 1
    
# annualized irr of t-bills
# bond equivalent yield
# Recall that yield to maturity is expressed as an annual percentage rate.
def bond_ey(irr, n):
    return irr * (365 / n)




# price_1 = treasury_bill(10000, 2.54, 81)
# # irr = t_bill_irr(98999, 100000)
# print(f't-bill price: {treasury_bill(10000, 2.54, 81)}')
# print(f'irr t-bill: {t_bill_irr(98999, 100000) * 100}')
# print(f'Bond Equivalent Yield t-bill: {bond_ey((irr/100), 54)}')
# print(f'effective annual yield {effective_annual_r(1.011, 54):.3%}')
print(f'value of bond: {coupon_bond(10, 4, 2, 1000, 5)}')
# print(f'ytm: {ytm_coupon(12, 1000, 1000, 5, 1)}')
# print(f'effective annual rate: {ear(12, 2, 2)}')
# print(f'yield zero coupon: {yield_to_m(1000, 744.09, 5)}')


# print(f'market value of the bond is: {zero_c(10000, 5.35, 1)}')
# print(f'Yield to maturity of the bond (anual compund) is: {yield_to_m(1000000, 455500, 20):.2%}')
# print(f'Yield to maturity of the bond (semi-anual compund) is: {yield_to_m(1000000, 455500, 40) * 2:.2%}')