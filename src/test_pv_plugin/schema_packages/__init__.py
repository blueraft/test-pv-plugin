from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from test_pv_plugin.schema_packages.schema_package import m_package

        return m_package


class fairmatPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from test_pv_plugin.schema_packages.fairmat_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


fairmat_schema_package_entry_point = fairmatPackageEntryPoint(
    name='fairmatPackage',
    description='fairmat package entry point configuration.',
)
