class Ohms:
    """A class representing basic electrical calculations based on Ohm's Law."""
    
    def voltage(self, I: float, R: float) -> float:
        """
        Calculate voltage using Ohm's Law.

        Parameters:
            I (float): The current in amperes.
            R (float): The resistance in ohms.

        Returns:
            float: The voltage in volts.
        """
        U = I * R
        return U
    
    def current(self, U: float, R: float) -> float:
        """
        Calculate current using Ohm's Law.

        Parameters:
            U (float): The voltage in volts.
            R (float): The resistance in ohms.

        Returns:
            float: The current in amperes.
        """
        I = U / R
        return I
        
    def resistance(self, U: float, I: float) -> float:
        """
        Calculate resistance using Ohm's Law.

        Parameters:
            U (float): The voltage in volts.
            I (float): The current in amperes.

        Returns:
            float: The resistance in ohms.
        """
        R = U / I
        return R
    
    def led_resistor(self, 
                    source: float,
                    led_voltage: float,
                    led_current: float = 0.02) -> float:
        
        """
        Calculate the resistor value needed for a LED circuit using Ohm's Law.

        This method calculates the resistor value needed to limit the current flowing through an LED
        to a specified value, considering the source voltage and the forward voltage drop of the LED.

        Parameters:
            source (float): The voltage of the power source in volts.
            led_voltage (float): The forward voltage of the LED in volts.
            led_current (float, optional): The desired current for the LED in amperes.
                                            Defaults to 0.02 (20mA).

        Returns:
            float: The resistance value needed for the LED circuit in ohms.
        """
        
        U = source - led_voltage
        return U/led_current
