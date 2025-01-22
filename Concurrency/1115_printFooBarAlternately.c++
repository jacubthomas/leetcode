/*
 * Difficulty Medium
 * Suppose you are given the following code:
 * class FooBar {
 *   public void foo() {
 *     for (int i = 0; i < n; i++) {
 *       print("foo");
 *     }
 *   }
 * 
 *   public void bar() {
 *     for (int i = 0; i < n; i++) {
 *       print("bar");
 *     }
 *   }
 * }
 * The same instance of FooBar will be passed to two different threads:
 *     thread A will call foo(), while
 *     thread B will call bar().
 * Modify the given program to output "foobar" n times.
 * 
 * Example 1:
 * Input: n = 1
 * Output: "foobar"
 * Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
 * "foobar" is being output 1 time.
 * 
 * Example 2:
 * Input: n = 2
 * Output: "foobarfoobar"
 * Explanation: "foobar" is being output 2 times.
 * 
 * Constraints:
 * 1 <= n <= 1000
*/

#include "condition_variable"
#include "functional"
#include "mutex"

using namespace std;

class FooBar {
private:
    int n;
    bool m_fooAvailable = true;
    bool m_barAvailable = false;
    condition_variable m_cv_foo;
    condition_variable m_cv_bar;
    mutex m_mutex;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            
            unique_lock<mutex> u_lock(m_mutex);
            m_cv_foo.wait(u_lock, [this] {
                return m_fooAvailable;
            });

        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();

            m_fooAvailable = false;
            m_barAvailable = true;

            m_cv_bar.notify_one();
            u_lock.unlock();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            
            unique_lock<mutex> u_lock(m_mutex);
            m_cv_bar.wait(u_lock, [this] {
                return m_barAvailable;
            });

        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();

            m_fooAvailable = true;
            m_barAvailable = false;

            m_cv_foo.notify_one();
            u_lock.unlock();
        }
    }
};