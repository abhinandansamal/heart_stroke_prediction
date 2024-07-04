from dataclasses import dataclasses

@dataclasses
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclasses
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path: str