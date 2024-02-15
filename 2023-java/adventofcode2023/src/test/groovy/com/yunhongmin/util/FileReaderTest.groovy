package com.yunhongmin.util

import spock.lang.Specification

class FileReaderTest extends Specification {
    def "ReadAll"() {
        given:
        def filepath = "file_reader_test1.txt"
        String absolutePath = FileReaderTest.class.getResource("/" + filepath).getFile()

        when:
        def actual = FileReader.readAll(absolutePath)

        then:
        def expected = ["abcd", "efgh", "ijk"]
        assert actual == expected

    }
}
