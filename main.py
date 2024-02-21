from enum import Enum

class CropStatus(Enum):
    SEED = "Seed"
    SEEDLING = "Seedling"
    YOUNG = "Young"
    MATURE = "Mature"
    OLD = "Old"

class CropType(Enum):
    GENERIC = "Generic"

class Crop:
    """A generic food crop"""
    def __init__(self, growth_rate: float, light_need: float, water_need: float) -> None:
        self._growth = 0
        self._days_growing = 0

        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = CropStatus.SEED
        self._type = CropType.GENERIC

    def grow(self, light: float, water: float):
        if light >= self._light_need and water >= self.water_need:
            # Provided amounts of light and water are adequate
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

    def generate_report(self):
        """Returns a dictionary of information about the crop's current state"""
        return {
            "type": self._type,
            "status": self._status,
            "growth": f"{self._growth} days growing"
        }

    def _update_status(self):
        """Changes the status of the crop based on its growth value"""
        if self.growth > 15:
            self._status = CropStatus.OLD
        elif self.growth > 10:
            self._status = CropStatus.OLD
        elif self.growth > 5:
            self._status = CropStatus.OLD
        elif self.growth > 0:
            self._status = CropStatus.OLD
        elif self.growth == 0:
            self._status = CropStatus.OLD
        else:
            raise ValueError(f"Crop growth value is invalid")

def main():
    new_crop = Crop(growth_rate=2, light_need=4, water_need=3)
    barley = Crop(growth_rate=3, light_need=6, water_need=4)

    new_crop.grow(light=6, water=6)
    print(new_crop.generate_report())

