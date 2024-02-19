#!/bin/bash

# Remove a textual watermark from a PDF file.  Requires qpdf and pdftx
# to work correctly.  The correct usage is
#
# remove-watermark WATERMARK "Your Input File.pdf" "Your Output File.pdf"

# https://gist.githubusercontent.com/elfsternberg/a96883018d783cbbad7b454ecd0a7ffe/raw/8a03d341c480324ad6611c0fd5150bb3ca10e16a/remove-watermark.sh
WATERMARK=$1
INBOUND=$2
OUTBOUND=$3



UNCOMPRESSED=`mktemp --dry-run 'uncompressed-XXXXXXXXXX.pdf'`
FIXED=`mktemp --dry-run 'fixed-XXXXXXXXXX.pdf'`
UNMARKED=`mktemp --dry-run 'unmarked-XXXXXXXXXX.pdf'`

WATERMARKLEN=${#WATERMARK}
BLANKS=`printf %${WATERMARKLEN}s`

qpdf --stream-data=uncompress "$INBOUND" $UNCOMPRESSED
sed -e "s%$WATERMARK%$BLANKS%g" < $UNCOMPRESSED > $FIXED
pdftk $FIXED output $UNMARKED
qpdf --stream-data=compress $UNMARKED "$OUTBOUND"
rm $UNCOMPRESSED $FIXED $UNMARKED

# NO WARRANTY
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.