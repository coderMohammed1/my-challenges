 void levlbyleve(Node r){
        ArrayList<Node> tracker = new ArrayList<Node>();
        tracker.add(r);
        System.out.println(tracker.get(0).value);
        int i =0;

        while(tracker.size() < size){
            if(tracker.get(i).left != null){
                tracker.add(tracker.get(i).left);
                System.out.println(tracker.get(i).left.value);
            }

            if(tracker.get(i).right != null){
                tracker.add(tracker.get(i).right);
                System.out.println(tracker.get(i).right.value);
            }

            i++;
        }

       // you can then do what ever you want with the arraylist
       // you can also use normal array if u wish 

    }
