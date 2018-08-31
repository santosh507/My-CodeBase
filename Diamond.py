class Device():
    pass

class OperationDevice(Device):
    def __init__(self):
        super(OperationDevice, self).__init__()

    def start(self):
        # Do operation specific code
        print('OperationDevice Started')

    def stop(self):
        # Do operation specific code
        print('OperationDevice Stopped')

class SimulationDevice(Device):
    def __init__(self):
        super(SimulationDevice, self).__init__()

    def start(self):
        # Do simulation specific code
        self.fsm.start()

    def stop(self):
        # Do simulation specific code
        self.fsm.stop()


class DualModeDevice(Device):
    def __init__(self, mode='simulation'):
        super(DualModeDevice, self).__init__()
        self._mode = mode
        self._mode_map = {
            'simulation': SimulationDevice(),
            'operation': OperationDevice()
        }

    def start(self):
        self._mode_map[self._mode].start()

    def stop(self):
        self._mode_map[self._mode].stop()