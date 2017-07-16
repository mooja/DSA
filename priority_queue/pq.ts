class PQ<T> {
    public pq: (T|null)[];
    constructor () {
        this.pq = [null];
    }

    insert(item: T): void {
        this.pq.push(item);
        this.swim();
    }

    remove_max(): T {
        const rv = this.pq[1];
        this.swap(1, this.pq.length-1);
        this.pq.pop();
        this.sink();
        return <T>rv;
    }

    private swim(): void {
        let idx = this.pq.length-1;
        while(idx > 1) {
            const parent_idx = Math.floor(idx / 2);
            const is_larger_than_parent: boolean = 
                <T>this.pq[idx] > <T>this.pq[parent_idx];
            if(!is_larger_than_parent) return;
            this.swap(idx, parent_idx);
            idx = parent_idx;
        }
    }

    private sink(): void {
        let idx = 1;
        let [child1_idx, child2_idx] = [idx*2, idx*2+1];
        while(child1_idx < this.pq.length - 1) {
            const only_one_child: boolean = child2_idx == this.pq.length - 1;
            if (only_one_child)  {
                if (<T>this.pq[idx] >= <T>this.pq[child1_idx]) 
                    return;
                this.swap(idx, child1_idx);
                idx = child1_idx;
                [child1_idx, child2_idx] = [idx*2, idx*2+1];
            }
            else {
                const child1 = <T>this.pq[child1_idx];
                const child2 = <T>this.pq[child2_idx];
                if (!(child1 > <T>this.pq[idx] || child2 > <T>this.pq[idx]))
                    return;
                const bigger_child_idx: number = child1 > child2 ? child1_idx : child2_idx;
                this.swap(idx, bigger_child_idx);
                idx = bigger_child_idx;
                [child1_idx, child2_idx] = [idx*2, idx*2+1];
            }
        }
    }

    private swap(idx1: number, idx2: number): void {
        const temp = <T>this.pq[idx1];
        this.pq[idx1] = this.pq[idx2];
        this.pq[idx2] = temp;
    }
}

const pq: PQ<number> = new PQ();
for (let i=0; i<10; i++)
    pq.insert(i);
pq.remove_max();
while (pq.pq.length > 1) {
    console.log(pq.remove_max());
}
console.log(pq.pq);