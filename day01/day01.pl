#! /usr/bin/env perl

use strict;
use warnings;

chomp($_ = <>);
print <<"";
Part 1: @{[eval join '+', 0, /(\d)(?=\1)/g, /^(\d).*\1$/]}
Part 2: @{[eval join '+', 0, (/(\d)(?=\d{@{[length() - 1 >> 1]}}\1)/g) x 2]}
