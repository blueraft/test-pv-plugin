from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from test_pv_plugin.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class fairmatExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from test_pv_plugin.parsers.fairmat_batch_parser import fairmatExperimentParser

        return fairmatExperimentParser(**self.model_dump())


class fairmatParserEntryPoint(ParserEntryPoint):

    def load(self):
        from test_pv_plugin.parsers.fairmat_measurement_parser import fairmatParser

        return fairmatParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


fairmat_experiment_parser_entry_point = fairmatExperimentParserEntryPoint(
    name='fairmatExperimentParserEntryPoint',
    description='fairmat experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


fairmat_parser_entry_point = fairmatParserEntryPoint(
    name='fairmatParserEntryPoint',
    description='fairmat parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
