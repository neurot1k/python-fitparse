import datetime


class FitFileDataProcessor(object):
    # TODO: Document API
    #def process_type_<type_name> (field_data)
    #def process_field_<field_name> (field_data) -- can be unknown_DD but NOT recommended
    #def process_message_<mesg_name / mesg_type_num> (data_message)

    @staticmethod
    def process_type_bool(field_data):
        if field_data.value is not None:
            field_data.value = bool(field_data.value)

    @staticmethod
    def process_type_date_time(field_data):
        value = field_data.value
        if value is not None and value >= 0x10000000:
            field_data.value = datetime.datetime.utcfromtimestamp(631065600 + value)
            field_data.units = None  # Units were 's', set to None

    @staticmethod
    def process_type_local_date_time(field_data):
        if field_data.value is not None:
            field_data.value = datetime.datetime.fromtimestamp(631065600 + field_data.value)
            field_data.units = None


class StandardUnitsDataProcessor(FitFileDataProcessor):
    @staticmethod
    def process_field_distance(field_data):
        if field_data.value is not None:
            field_data.value /= 1000.0
        field_data.units = 'km'

    @staticmethod
    def process_field_speed(field_data):
        if field_data.value is not None:
            field_data.value /= 1000.0
        field_data.units = 'm/s'

    @staticmethod
    def process_field_altitude(field_data):
        if field_data.value is not None:
            field_data.value = (field_data.value / 5.0) - 500
        field_data.units = 'm'

    @staticmethod
    def process_units_semicircles(field_data):
        if field_data.value is not None:
            field_data.value *= 180.0 / (2 ** 31)
        field_data.units = 'deg'
