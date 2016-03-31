#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
default_app_config = 'calaccess_raw.apps.CalAccessRawConfig'


def get_download_directory():
    """
    Returns the download directory where we will store downloaded data.
    """
    if hasattr(settings, 'CALACCESS_DOWNLOAD_DIR'):
        return getattr(settings, 'CALACCESS_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'data')
    raise ValueError("CAL-ACCESS download directory not configured. Set either \
CALACCESS_DOWNLOAD_DIR or BASE_DIR in settings.py")


def get_test_download_directory():
    """
    Returns the download directory where we will store test data.
    """
    if hasattr(settings, 'CALACCESS_TEST_DOWNLOAD_DIR'):
        return getattr(settings, 'CALACCESS_TEST_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'test-data')
    raise ValueError("CAL-ACCESS test download directory not configured. \
Set either CALACCESS_TEST_DOWNLOAD_DIR or BASE_DIR in settings.py")


def archive_directory_path(instance, filename):
    """
    Returns a path to an archived RawDataFile (e.g.,
    MEDIA_ROOT/YYYY-MM-DD_HH-MM-SS/filename.ext)
    """
    from calaccess_raw.models.tracking import RawDataVersion, RawDataFile

    if isinstance(instance, RawDataVersion):
        release_datetime = instance.release_datetime
    elif isinstance(instance, RawDataFile):
        release_datetime = instance.version.release_datetime
    else:
        raise TypeError("Must be called on an instance of RawDataVersion "
                        "or RawDataFile.")
    return '{dt.year}-{dt.month}-{dt.day}_{dt.hour}-{dt.minute}-{dt.second}/{f}'.format(
            dt=release_datetime,
            f=filename
        )


def get_model_list():
    """
    Returns a model list with all the data tables in this application
    """
    from django.apps import apps
    models = []

    for model in apps.get_app_config("calaccess_raw").models.values():
        # ignore models that don't inherit from CalAccessBaseModel
        if "CalAccessBaseModel" in str(model.__base__):
            models.append(model)

    return models


def get_sorted_choices(codes_dict):
    """
    Returns a tuple of tuples, sorted by the given codes_dict's key
    """
    return tuple(sorted(codes_dict.items(), key=lambda x: x[0]))
