package com.yunhongmin.day01

import spock.lang.Specification

class Solution1Test extends Specification {
    def "FindCalibrationValue"() {
        when:
        def actual = Solution1.findCalibrationValue(input)

        then:
        assert actual == expected

        where:
        input         || expected
        "1"           || 11
        "123"         || 13
        "1abc2"       || 12
        "pqr3stu8vwx" || 38
        "a1b2c3d4e5f" || 15
        "treb7uchet"  || 77
    }
}
