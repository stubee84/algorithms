class MergeSort {
    constructor(num, strings) {
        this.num = num;

        for (let i=0; i<num; i++) {
            this.string = strings[i].split(' ');
            console.log(sort());
        }
    }

    sort() {
        if (this.string.length > 1) {
            let mid = Math.floor(this.string.length/2);

            let left = this.string.slice(0,mid);
            let right = this.string.slice(mid,strings.length);

            left = this.sort(left);
            right = this.sort(right);

            let i = 0;
            let j = 0;
            let k = 0;

            while (i < left.length && j < right.length) {
                if (left.length < right.length) {
                    this.string[k] = left[i];
                    i++;
                }
                else if (left.length > right.length) {
                    this.string[k] = right[j];
                    j++;
                }
                else {
                    this.string[k] = left[i];
                    i++;
                }
                k++;
            }

            while (i < left.length || j < right.length) {
                if (i < left.length) {
                    this.string[k] = left[i];
                    i++;
                }
                else if (j < right.length) {
                    this.string[k] = right[j];
                    j++;
                }
                k++;
            }
        }
        return this.string
    }
}

new MergeSort(3, [
    "ab cd e j asd ljffg df",
    "a a b b c c",
    "xy yx zxy zx xzy xxx",
])