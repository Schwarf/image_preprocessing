from data_access.files.interfaces.i_file_access import IFileAccess
from pure_interface import Interface

from source.data_access.interfaces.i_data_source import IDataSource


class IFileReader(IDataSource, IFileAccess, Interface):
    pass
