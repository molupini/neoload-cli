import click

from commands import test_settings, test_results
from neoload_cli_lib import user_data


@click.command()
def cli():
    """get status of NeoLoad cli Settings"""
    login = user_data.get_user_data(False)
    if login is None:
        print("No settings is stored. Please use \"neoload login\" to start.")
    else:
        print(augment_with_names(login))
    pass

def augment_with_names(data):
    output = str(data)

    if test_settings.is_current_test_settings_set():
        json = test_settings.get_current_test_settings_json()
        settings_id = data.metadata[test_settings.meta_key]
        output = output.replace(settings_id,settings_id + " ({name})".format(**json))

    if test_results.is_current_test_results_set():
        json = test_results.get_current_test_results_json()
        results_id = data.metadata[test_results.meta_key]
        output = output.replace(results_id,results_id + " ({project}|{scenario}|{name}) {status}|{qualityStatus}".format(**json))

    return output
