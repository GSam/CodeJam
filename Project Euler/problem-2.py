import decimal
from decimal import Decimal
import math

def arbitrary_precision_sqrt(S, precision):
    """
    Computes the square root of S to the specified decimal precision 
    using the Newton-Raphson method.
    """
    # Convert input to Decimal
    S = Decimal(S)

    # Handle base cases
    if S < 0:
        raise ValueError("Cannot compute the square root of a negative number in the real domain.")
    if S == 0:
        return Decimal(0)

    # We run intermediate calculations with 5 extra guard digits
    # to prevent rounding errors from affecting the final digit.
    extra_precision = precision + 5

    with decimal.localcontext() as ctx:
        ctx.prec = extra_precision

        # 1. Generate an initial guess (x0) using the scale of S.
        # This keeps the initial guess close to the actual root,
        # avoiding slow convergence for extremely large/small values.
        sign, digits, exponent = S.as_tuple()
        scale = exponent + len(digits) - 1
        x_curr = Decimal(10) ** (scale // 2)

        # Calculate maximum iterations needed. Since correct digits double
        # each step, we need roughly log2(precision) iterations.
        max_iterations = int(math.log2(precision)) + 5

        x_prev = None
        half = Decimal('0.5')

        # 2. Newton-Raphson iteration loop
        for _ in range(max_iterations):
            x_next = half * (x_curr + S / x_curr)

            # Stop if we have reached the limit of our precision.
            # We check both x_curr and x_prev to handle minor 1-ULP oscillations.
            if x_next == x_curr or x_next == x_prev:
                x_curr = x_next
                break

            x_prev = x_curr
            x_curr = x_next

    # 3. Restore standard context and round the final result to the target precision
    with decimal.localcontext() as ctx:
        ctx.prec = precision
        # Perform a unary plus operation to apply the precision rounding
        return +x_curr

if __name__ == "__main__":
    # Example 1: Square root of 2 to 50 decimal places
    sqrt_2 = arbitrary_precision_sqrt(2, 50)
    print(f"sqrt(2) to 50 places:\n{sqrt_2}\n")

    # Example 2: Square root of an extremely large number
    large_num = "123456789012345678901234567890" * 2
    sqrt_large = arbitrary_precision_sqrt(large_num, 30)
    print(f"sqrt(Large Number) to 30 places:\n{sqrt_large}\n")

    # Example 3: Square root of an extremely small number
    small_num = "0.0000000000000000000000000000000000000012345"
    sqrt_small = arbitrary_precision_sqrt(small_num, 40)
    print(f"sqrt(Small Number) to 40 places:\n{sqrt_small}")
    print(arbitrary_precision_sqrt(13, 1001))

print(sum(int(x) for x in '6055512754639892931192212674704959462512965738452462127104530562271669482930104452046190820184907176735141820240635403760306782646978077051630171668927097577426905642741526332338303949623469447962732299962880032688564272130721127331690722052975017855588384448146538689210753953924825633102446828366387325286968101892633130498355399216211744108618057015127689031028812143994831798683809191329034353620627951223336511358206979573836238526577606890679260960318450063056151264019838072555225488043999506806390960914463179762891635645447196853921690689156698918467597390353947698499962247909644289010644441276675481640212983715961814894472819793817321444784645781139649705695246073687480703027957221161404880328817165955719615176191267450711335387328533605451035213805566502555494587073292081260347734391582994367395751429587741287176131489832849136748198228867067050088735729856451832081359575583745287489977704982250744917394861221499173463141297785305679365833859084923735540651072975297023582252157988'))
