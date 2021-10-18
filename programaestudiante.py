import argparse
from pyspark.sql import SparkSession

def spark_session():
    spark = SparkSession.builder.appName("Bigdata: Tarea 2").getOrCreate()
    return spark

def get_parser():
    parser = argparse.ArgumentParser('Tarea2')
    parser.add_argument('--folder', '-f', type=str, help='Folder que contiene todos los archivos *.json ', required=True)
    return parser

def total_productos():
    print("Generate file 'total_productos.csv'")

def total_cajas():
    print("Generate file 'total_cajas.csv'")

def metricas():
    print("Generate file 'metricas.csv'")

def main(args=None):
    parser = get_parser()
    args = parser.parse_args(args)
    print(args.folder)

    # schema = ['numero_caja','compras']

    spark = spark_session()

    df = spark.read.option("multiline","true").json(args.folder)
    df.printSchema()
    df.show()


if __name__ == '__main__':
    main()