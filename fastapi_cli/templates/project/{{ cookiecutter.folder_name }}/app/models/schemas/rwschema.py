from app.models.domain.rwmodel import RWModel
from app.models.common import PeeweeGetterDict

class RWSchema(RWModel):
    class Config(RWModel.Config):
        orm_mode = True
        getter_dict = PeeweeGetterDict
