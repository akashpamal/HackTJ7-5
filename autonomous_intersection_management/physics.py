class Physics:
    def get_position(self, a, timeofAcc dtAcc, elapsed_time):
        

        if elapsed_time <= timeofAcc:
            return initV*elapsed_time
        elif elapsed_time <= (timeofAcc+dt):
            initV*timeofAcc + 

            elapsed_time-timeofAcc
            (initV*(elapsed_time-timeofAcc) + (0.5*a*(elapsed_time-timeofAcc))



        dX2 = (initV*(dtAcc) + (0.5*a*(dtAcc**2))

        dX3 = finalV*(exitTime-endofAcc)


        return dX1 + dX2 + dX3
