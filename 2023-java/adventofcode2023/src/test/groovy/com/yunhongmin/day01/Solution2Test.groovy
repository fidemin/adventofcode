package com.yunhongmin.day01

import spock.lang.Specification

class Solution2Test extends Specification {
    def "FindCalibrationValue"() {
        when:
        def actual = Solution2.findCalibrationValue(input)

        then:
        assert actual == expected

        where:
        input                 || expected
        // only digit test
        "1"                   || 11
        "123"                 || 13
        "1abc2"               || 12
        "pqr3stu8vwx"         || 38
        "a1b2c3d4e5f"         || 15
        "treb7uchet"          || 77
        // only string test
        "one"                 || 11
        "otwo"                || 22
        "oneight"             || 18
        "eighthreeight"       || 88
        "aaaeighthreeightaaa" || 88
        // complex
        "two1nine"            || 29
        "xtwone3fff"          || 23
        "ddd3oneight"         || 38
        "4nineeightseven2"    || 42
    }
}
