import argparse
import pytest
from pyspark.sql import SparkSession

def spark_session():
    """A fixture to create a Spark Context to reuse across tests."""
    s = SparkSession.builder.appName('pytest-local-spark').master('local') \
        .getOrCreate()

    yield s

    s.stop()
    return s

def get_parser():
    parser = argparse.ArgumentParser('Tarea1')
    parser.add_argument('--curso', '-c', type=str, help='Cursos .csv', required=True)
    parser.add_argument('--estudiante', '-e', type=str, help='Estudiantes .csv', required=True)
    parser.add_argument('--nota', '-n', type=str, help='Notas .csv', required=True)
    return parser

def main(args=None):
    parser = get_parser()
    args = parser.parse_args(args)
    print(args.curso)
    print(args.estudiante)
    print(args.nota)
    s = spark_session()

    curso_df = s.read(args.curso).format("csv").option("header", "false")
    curso_df.printSchema()

if __name__ == '__main__':
    main()