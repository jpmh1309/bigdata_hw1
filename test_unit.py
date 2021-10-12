def test_sum_two_correctly(spark_session):
    grades_data = [(1, 50), (2, 100)]
    grades_ds = spark_session.createDataFrame(grades_data,
                                              ['student_id', 'grade'])
    student_data = [(1, 'Juan'), (2, 'Maria')]
    student_ds = spark_session.createDataFrame(student_data,
                                               ['id', 'name'])

    grades_ds.show()
    student_ds.show()
    assert 2 + 2 == 4


def test_sum_two_incorrectly(spark_session):
    # Expected to fail. Replace by
    # assert 3 + 3 == 6
    grades_data = [(1, 50), (2, 100)]
    grades_ds = spark_session.createDataFrame(grades_data,
                                              ['student_id', 'grade'])
    student_data = [(1, 'Juan'), (2, 'Maria')]
    student_ds = spark_session.createDataFrame(student_data,
                                               ['id', 'name'])

    grades_ds.show()
    student_ds.show()
    assert 3 + 3 == 5
